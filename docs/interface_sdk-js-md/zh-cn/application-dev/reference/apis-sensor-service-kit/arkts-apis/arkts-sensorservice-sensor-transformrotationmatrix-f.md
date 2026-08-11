# transformRotationMatrix

## transformRotationMatrix

```TypeScript
function transformRotationMatrix(inRotationVector: Array<double>, coordinates: CoordinatesOptions,
    callback: AsyncCallback<Array<double>>): void
```

根据指定坐标系映射旋转矩阵，使用Callback异步方式返回结果。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-sensor-function transformRotationMatrix(inRotationVector: Array<double>, coordinates: CoordinatesOptions,    callback: AsyncCallback<Array<double>>): void--><!--Device-sensor-function transformRotationMatrix(inRotationVector: Array<double>, coordinates: CoordinatesOptions,    callback: AsyncCallback<Array<double>>): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inRotationVector | ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;double&gt; | 是 | 旋转矩阵。 |
| coordinates | [CoordinatesOptions](arkts-sensorservice-sensor-coordinatesoptions-i.md) | 是 | 指定坐标系方向。 |
| callback | ArkTS-Dyn: [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;number&gt;&gt;  <br>ArkTS-Sta：[AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;double&gt;&gt; | 是 | 回调函数，异步返回映射后的旋转矩阵。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) | Service exception. Possible causes: 1. Sensor hdf service exception; &lt;br&gt; 2. Sensor service ipc exception;3. Sensor data channel exception. |

## 示例

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sensor } from '@kit.SensorServiceKit';

// 使用try catch对可能出现的异常进行捕获
try {
  let rotationMatrix = [
    1, 0, 0,
    0, 0.87, -0.50,
    0, 0.50, 0.87
  ];
  sensor.transformRotationMatrix(rotationMatrix, { x: 1, y: 3 }, (err, data) => {
    let error = err as BusinessError;
    let dataValue = data as Array<number>;
    if (error) {
      console.error(`Failed to transform rotationMatrix. Code: ${error.code}, message: ${error.message}`);
      return;
    }
    for (let i = 0; i < dataValue.length; i++) {
      console.info('Succeeded in getting data[' + i + '] = ' + dataValue[i]);
    }
  })
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to transform rotationMatrix. Code: ${e.code}, message: ${e.message}`);
}
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sensor } from '@kit.SensorServiceKit';

// 使用try catch对可能出现的异常进行捕获
try {
  let rotationMatrix = [
    1, 0, 0,
    0, 0.87, -0.50,
    0, 0.50, 0.87
  ];
  sensor.transformRotationMatrix(rotationMatrix, { x: 1, y: 3 }, (err, data) => {
    let error = err as BusinessError;
    let dataValue = data as Array<double>;
    if (error) {
      console.error(`Failed to transform rotationMatrix. Code: ${error.code}, message: ${error.message}`);
      return;
    }
    for (let i = 0; i < dataValue.length; i++) {
      console.info('Succeeded in getting data[' + i + '] = ' + dataValue[i]);
    }
  })
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to transform rotationMatrix. Code: ${e.code}, message: ${e.message}`);
}
```


## transformRotationMatrix

```TypeScript
function transformRotationMatrix(inRotationVector: Array<double>, coordinates: CoordinatesOptions): Promise<Array<double>>
```

根据指定坐标系映射旋转矩阵，使用Promise异步方式返回结果。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-sensor-function transformRotationMatrix(inRotationVector: Array<double>, coordinates: CoordinatesOptions): Promise<Array<double>>--><!--Device-sensor-function transformRotationMatrix(inRotationVector: Array<double>, coordinates: CoordinatesOptions): Promise<Array<double>>-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inRotationVector | ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;double&gt; | 是 | 旋转矩阵。 |
| coordinates | [CoordinatesOptions](arkts-sensorservice-sensor-coordinatesoptions-i.md) | 是 | 指定坐标系方向。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: Promise&lt;Array&lt;number&gt;&gt;  <br>ArkTS-Sta：Promise&lt;Array&lt;double&gt;&gt; | Promise对象，使用异步方式返回转换后的旋转矩阵。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) | Service exception. Possible causes: 1. Sensor hdf service exception; &lt;br&gt; 2. Sensor service ipc exception;3. Sensor data channel exception. |

