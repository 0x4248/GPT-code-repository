import java.io.File;
import java.io.IOException;
import javax.sound.sampled.AudioFileFormat;
import javax.sound.sampled.AudioFormat;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.UnsupportedAudioFileException;
import edu.emory.mathcs.jtransforms.fft.DoubleFFT_1D;

public class MusicGenreClassifier {
    private static final int NUM_SAMPLES = 1024;
    private static final int NUM_MFCC_COEFFS = 13;
    private static final int NUM_SPECTRAL_FEATURES = 128;

    private static final double[][] MFCC_FILTER_BANK = {
            {0.0, 1.0, 0.0, 0.0},
            {0.5, 0.5, 0.0, 0.0},
            {0.2, 0.6, 0.2, 0.0},
            {0.1, 0.3, 0.4, 0.2},
            {0.1, 0.2, 0.3, 0.4},
            {0.2, 0.4, 0.2, 0.2},
            {0.2, 0.2, 0.2, 0.4},
            {0.3, 0.4, 0.3, 0.0},
            {0.3, 0.3, 0.3, 0.1},
            {0.1, 0.1, 0.1, 0.7},
            {0.1, 0.1, 0.7, 0.1},
            {0.1, 0.7, 0.1, 0.1},
            {0.7, 0.1, 0.1, 0.1}
    };

    public static void main(String[] args) throws IOException, UnsupportedAudioFileException {
        if (args.length != 1) {
            System.out.println("Usage: java MusicGenreClassifier <audio_file>");
            return;
        }

        String filePath = args[0];
        File audioFile = new File(filePath);

        if (!audioFile.exists()) {
            System.out.println("File not found: " + filePath);
            return;
        }

        AudioInputStream audioInputStream = AudioSystem.getAudioInputStream(audioFile);
        AudioFormat audioFormat = audioInputStream.getFormat();

        if (audioFormat.getEncoding() != AudioFormat.Encoding.PCM_SIGNED) {
            System.out.println("Unsupported audio format: " + audioFormat);
            return;
        }

        int numChannels = audioFormat.getChannels();
        int sampleRate = (int) audioFormat.getSampleRate();
        int numBytesPerSample = audioFormat.getSampleSizeInBits() / 8;

        byte[] audioData = new byte[NUM_SAMPLES * numChannels * numBytesPerSample];
        int numBytesRead = audioInputStream.read(audioData);

        if (numBytesRead < audioData.length) {
            System.out.println("End of file reached unexpectedly.");
            return;
        }
    double[] audioSamples = new double[NUM_SAMPLES];
    double[] audioSamplesMono = new double[NUM_SAMPLES];
    double[] audioSamplesWindowed = new double[NUM_SAMPLES];
    double[] audioSpectrum = new double[NUM_SAMPLES / 2 + 1];
    double[] audioMFCC = new double[NUM_MFCC_COEFFS];
    double[] audioSpectralFeatures = new double[NUM_SPECTRAL_FEATURES];

    // convert byte array to double array
    for (int i = 0; i < NUM_SAMPLES; i++) {
        for (int j = 0; j < numChannels; j++) {
            int byteIndex = i * numBytesPerSample * numChannels + j * numBytesPerSample;
            int sampleValue = 0;
            for (int k = 0; k < numBytesPerSample; k++) {
                sampleValue |= (audioData[byteIndex + k] & 0xff) << (k * 8);
            }
            audioSamples[i] += (double) sampleValue / (1 << (numBytesPerSample * 8 - 1));
        }
        audioSamples[i] /= numChannels;
        audioSamplesMono[i] = audioSamples[i];
    }

    // apply window function to audio samples
    for (int i = 0; i < NUM_SAMPLES; i++) {
        double windowValue = 0.5 * (1 - Math.cos(2 * Math.PI * i / (NUM_SAMPLES - 1)));
        audioSamplesWindowed[i] = audioSamplesMono[i] * windowValue;
    }

    // compute FFT of windowed audio samples
    DoubleFFT_1D fft = new DoubleFFT_1D(NUM_SAMPLES);
    fft.realForward(audioSamplesWindowed);
    for (int i = 0; i < audioSpectrum.length; i++) {
        audioSpectrum[i] = Math.sqrt(audioSamplesWindowed[2*i] * audioSamplesWindowed[2*i] + audioSamplesWindowed[2*i+1] * audioSamplesWindowed[2*i+1]);
    }

    // compute MFCC coefficients from audio spectrum
    double[] melFilterBank = new double[NUM_SPECTRAL_FEATURES];
    for (int i = 0; i < NUM_MFCC_COEFFS; i++) {
        double sum = 0;
        for (int j = 0; j < NUM_SPECTRAL_FEATURES; j++) {
            int binIndex = (int) Math.floor((double) sampleRate * j / NUM_SAMPLES);
            melFilterBank[j] = audioSpectrum[binIndex] * MFCC_FILTER_BANK[j][i];
            sum += melFilterBank[j];
        }
        audioMFCC[i] = Math.log10(sum);
    }

    // compute spectral features from audio spectrum
    for (int i = 0; i < NUM_SPECTRAL_FEATURES; i++) {
        int binIndex = (int) Math.floor((double) sampleRate * i / NUM_SAMPLES);
        audioSpectralFeatures[i] = audioSpectrum[binIndex];
    }

    // TODO: load machine learning model and use it to classify audio file into music genre

    System.out.println("Music genre classification complete.");
}

