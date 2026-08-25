# initialize

## 导入模块

```TypeScript
import { connectedTag } from 'kits/@kit.ConnectivityKit';
```

## initialize

```TypeScript
function initialize(): void
```

初始化有源标签芯片。对有源标签进行读写操作前需调用本接口初始化一次，若想再次初始化需先调用[uninitialize](arkts-connectivity-connectedtag-uninitialize-f.md)。

**起始版本：** 9

**需要权限：** ohos.permission.NFC_TAG

**系统能力：** SystemCapability.Communication.ConnectedTag

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3200101](../errorcode-nfc.md#3200101-有源nfc标签状态异常) |
