import numpy as np

def get_data(save = False):
    def gamma_curve(t, amplitude, time_to_max, scale):
        return amplitude * (t ** (time_to_max - 1)) * np.exp(-t / scale) / (scale ** time_to_max)
    
    # Simulation parameters
    time = np.linspace(0, 1, 1000)  
    scale = 0.2 
    noise_level = 20  
    num_repetitions = 100
    
    amp1 = 15
    time_to_max1 = 3  
    
    amp2 = 2.0
    time_to_max2 = 5 
    
    signals1 = np.zeros((num_repetitions, len(time)))
    signals2 = np.zeros((num_repetitions, len(time)))
    
    evoked_potential1 = gamma_curve(time, amp1, time_to_max1, scale)
    evoked_potential2 = gamma_curve(time, amp2, time_to_max2, scale)
    
    for i in range(num_repetitions):
        noise1 = noise_level * np.random.normal(size=time.shape)
        noise2 = noise_level * np.random.normal(size=time.shape)
        signals1[i] = evoked_potential1 + noise1
        signals2[i] = evoked_potential2 + noise2*1.5

    signals1 /= 10
    signals2 /= 10

    if save:
        np.savetxt("condition1.txt", signals1)
        np.savetxt("condition2.txt", signals2)
        return signals1, signals2
    else:
        return signals1, signals2
