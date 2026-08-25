# removeAppShareOptions

## 导入模块

```TypeScript
import { unifiedDataChannel } from 'kits/@kit.ArkData';
```

## removeAppShareOptions

```TypeScript
function removeAppShareOptions(intention: Intention): void
```

清除[setAppShareOptions](arkts-arkdata-unifieddatachannel-setappshareoptions-f.md)设置的管控信息。调用成功后，setAppShareOptions设置的管控信息被清除，应用内拖 拽通道数据恢复到默认使用范围。

**起始版本：** 14

**需要权限：** 
- API版本14+：ohos.permission.MANAGE_UDMF_APP_SHARE_OPTION

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [intention](arkts-arkdata-unifieddatachannel-options-i.md) | [Intention](arkts-arkdata-unifieddatachannel-intention-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
