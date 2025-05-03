import tensorflow as tf

# class build:
#     @staticmethod
#     def build_it():
#         model = tf.keras.Sequential([
#             tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
#             tf.keras.layers.MaxPooling2D((2, 2)),
#             tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
#             tf.keras.layers.MaxPooling2D((2, 2)),
#             tf.keras.layers.Flatten(),
#             tf.keras.layers.Dense(64, activation='relu'),
#             tf.keras.layers.Dense(10, activation='softmax')
#         ])
#         model.compile(
#             optimizer='adam',
#             loss='sparse_categorical_crossentropy',
#             metrics=['accuracy', tf.keras.metrics.Mean(name='loss')]
#         )
#         return model
    
## Dany  ejemplo 
class build:
    @staticmethod
    def build_it():
        model = tf.keras.Sequential([
            tf.keras.layers.Input(shape=(28, 28, 1)),
            
            tf.keras.layers.Conv2D(16, (3, 3), activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)),
            tf.keras.layers.BatchNormalization(),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Dropout(0.5),
            
            tf.keras.layers.Conv2D(8, (3, 3), activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)),
            tf.keras.layers.BatchNormalization(),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Dropout(0.5),
            
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(16, activation='relu'),
            tf.keras.layers.Dense(10, activation='softmax')
        ])
        model.compile(
            optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )
        return model
    
"""
# David
class build:
    @staticmethod
    def build_it():
        model = tf.keras.Sequential([
            tf.keras.layers.Input(shape=(28, 28, 1)),
            
            tf.keras.layers.Conv2D(32, (3, 3), activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)),
            tf.keras.layers.BatchNormalization(),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Dropout(0.5),
            
            tf.keras.layers.Conv2D(16, (3, 3), activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)),
            tf.keras.layers.BatchNormalization(),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Dropout(0.5),
            
            tf.keras.layers.GlobalAveragePooling2D(),
            tf.keras.layers.Dense(64, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)),
            tf.keras.layers.BatchNormalization(),
            tf.keras.layers.Dropout(0.5),
            tf.keras.layers.Dense(10, activation='softmax')
        ])
        model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )
        return model
#"""