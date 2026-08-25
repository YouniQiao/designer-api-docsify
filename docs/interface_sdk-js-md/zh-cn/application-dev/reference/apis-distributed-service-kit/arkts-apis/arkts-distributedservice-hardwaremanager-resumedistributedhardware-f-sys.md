# resumeDistributedHardware（系统接口）

## 导入模块

```TypeScript
import { hardwareManager } from 'kits/@kit.DistributedServiceKit';
```

## resumeDistributedHardware

```TypeScript
function resumeDistributedHardware(description: HardwareDescriptor): Promise<void>
```

恢复被控端分布式硬件业务。使用promise异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.ACCESS_DISTRIBUTED_HARDWARE

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
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 24200101 |
| 24200102 |
