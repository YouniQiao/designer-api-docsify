# setAppShareOptions

## 导入模块

```TypeScript
import { unifiedDataChannel } from 'kits/@kit.ArkData';
```

## setAppShareOptions

```TypeScript
function setAppShareOptions(intention: Intention, shareOptions: ShareOptions): void
```

设置应用内拖拽通道数据可使用的范围[ShareOptions](arkts-arkdata-unifieddatachannel-shareoptions-e.md)，目前仅支持DRAG类型数据通道的管控设置。调用成功后，应用内拖拽通道数据的使用范围被设 置为指定的ShareOptions值。

**起始版本：** 14

**需要权限：** 
- API版本14+：ohos.permission.MANAGE_UDMF_APP_SHARE_OPTION

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [intention](arkts-arkdata-unifieddatachannel-options-i.md) | [Intention](arkts-arkdata-unifieddatachannel-intention-e.md) | 是 |
| [shareOptions](arkts-arkdata-unifieddatachannel-unifieddataproperties-c.md) | [ShareOptions](arkts-arkdata-unifieddatachannel-shareoptions-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [20400001](../errorcode-udmf.md#20400001-设置已存在若要重新配置请删除现有的共享选项) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
