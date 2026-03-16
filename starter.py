import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.DataFrame({'x': np.linspace(0, 10, 100)})
    df['y'] = np.sin(df['x'])
    print(df.head())
    plt.plot(df['x'], df['y'])
    plt.title('sin(x)')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.tight_layout()
    plt.savefig('plot.png')
    print('Saved plot.png')

if __name__ == '__main__':
    main()
