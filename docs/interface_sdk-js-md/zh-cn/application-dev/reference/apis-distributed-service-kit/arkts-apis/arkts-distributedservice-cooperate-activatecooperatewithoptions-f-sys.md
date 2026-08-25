# activateCooperateWithOptions（系统接口）

## 导入模块

```TypeScript
import { cooperate } from 'kits/@kit.DistributedServiceKit';
```

## activateCooperateWithOptions

```TypeScript
function activateCooperateWithOptions(targetNetworkId: string, inputDeviceId: number,
    cooperateOptions?: CooperateOptions
  ): Promise<void>
```

启动键鼠穿越，使用选项开始屏幕跳转。

**起始版本：** 20

**需要权限：** ohos.permission.COOPERATE_MANAGER

**系统能力：** SystemCapability.Msdp.DeviceStatus.Cooperate

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| targetNetworkId | string | 是 |
| inputDeviceId | number | 是 |
| cooperateOptions | [CooperateOptions](arkts-distributedservice-cooperate-cooperateoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [20900001](../errorcode-devicestatus.md#20900001-操作输入设备失败) |
