# createDeviceManager（系统接口）

## createDeviceManager

```TypeScript
function createDeviceManager(bundleName: string, callback: AsyncCallback<DeviceManager>): void
```

创建一个设备管理器实例。

**起始版本：** 7

**废弃版本：** 11

**替代接口：** [createDeviceManager](arkts-distributedservice-distributeddevicemanager-createdevicemanager-f.md#createDeviceManager)

<!--Device-deviceManager-function createDeviceManager(bundleName: string, callback: AsyncCallback<DeviceManager>): void--><!--Device-deviceManager-function createDeviceManager(bundleName: string, callback: AsyncCallback<DeviceManager>): void-End-->

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DeviceManager&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import deviceManager from '@ohos.distributedHardware.deviceManager';
import { BusinessError } from '@ohos.base';

let dmInstance: deviceManager.DeviceManager | null = null;
try {
  deviceManager.createDeviceManager("ohos.samples.jshelloworld", (err: BusinessError, data: deviceManager.DeviceManager) => {
    if (err) { 
      console.error("createDeviceManager errCode:" + err.code + ",errMessage:" + err.message);
      return;
    }
    console.info("createDeviceManager success");
    dmInstance = data;
  });
} catch(err) {
  let e: BusinessError = err as BusinessError;
  console.error("createDeviceManager errCode:" + e.code + ",errMessage:" + e.message);
}
```
