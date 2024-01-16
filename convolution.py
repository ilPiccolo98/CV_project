import numpy as np


def convolution(image: np.ndarray, kernel: list | tuple) -> np.ndarray:
    if len(image.shape) == 3:
        m_i, n_i, c_i = image.shape
    elif len(image.shape) == 2:
        image = image[..., np.newaxis]
        m_i, n_i, c_i = image.shape
    else:
        raise Exception('Shape of image not supported')
    m_k, n_k = kernel.shape
    y_strides = m_i - m_k + 1
    x_strides = n_i - n_k + 1
    img = image.copy()
    output_shape = (m_i-m_k+1, n_i-n_k+1, c_i)
    output = np.zeros(output_shape, dtype=np.float32)
    count = 0
    output_tmp = output.reshape((output_shape[0] * output_shape[1], output_shape[2]))
    for i in range(y_strides):
        for j in range(x_strides):
            for c in range(c_i):
                sub_matrix = img[i:i+m_k, j:j+n_k, c]
                output_tmp[count, c] = np.sum(sub_matrix * kernel)
            count += 1
    output = output_tmp.reshape(output_shape)
    return output