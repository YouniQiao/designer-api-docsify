# enableNfc

## 导入模块

```TypeScript
import { nfcController } from '@kit.ConnectivityKit';
```

## enableNfc

```TypeScript
function enableNfc(): void
```

打开NFC开关，该接口只能被系统应用调用。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_SECURE_SETTINGS

**系统能力：** SystemCapability.Communication.NFC.Core

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3100101](../errorcode-nfc.md#3100101-开关nfc异常) |
