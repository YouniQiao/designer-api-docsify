# resumeDistributedHardware（系统接口）

## resumeDistributedHardware

```TypeScript
function resumeDistributedHardware(description: HardwareDescriptor): Promise<void>
```

恢复被控端分布式硬件业务。使用promise异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.ACCESS_DISTRIBUTED_HARDWARE

<!--Device-hardwareManager-function resumeDistributedHardware(description: HardwareDescriptor): Promise<void>--><!--Device-hardwareManager-function resumeDistributedHardware(description: HardwareDescriptor): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedHardware.DistributedHardwareFWK

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| description | [HardwareDescriptor](arkts-distributedservice-hardwaremanager-hardwaredescriptor-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| 24200101 |
| 24200102 |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { hardwareManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let description: hardwareManager.HardwareDescriptor = {
    type: 1, // 分布式硬件类型，1表示相机
    srcNetworkId: '1111' // 源端设备网络ID
  };
  hardwareManager.resumeDistributedHardware(description).then(() => { // 恢复分布式硬件业务
    console.info('resume distributed hardware successfully');
  }).catch((error: BusinessError) => {
    console.error(`resume distributed hardware failed, cause: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`resume distributed hardware failed, code: ${err.code}, message: ${err.message}`);
}
```
