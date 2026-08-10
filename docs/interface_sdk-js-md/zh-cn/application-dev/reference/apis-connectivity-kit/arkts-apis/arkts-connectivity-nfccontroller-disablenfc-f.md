# disableNfc

## 导入模块

```TypeScript
import { nfcController } from 'kits/@kit.ConnectivityKit';
```

## disableNfc

```TypeScript
function disableNfc(): void
```

Disables NFC.This API can be called only by system applications

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_SECURE_SETTINGS

<!--Device-nfcController-function disableNfc(): void--><!--Device-nfcController-function disableNfc(): void-End-->

**系统能力：** SystemCapability.Communication.NFC.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 3100101 | The NFC state is abnormal in the service. |

