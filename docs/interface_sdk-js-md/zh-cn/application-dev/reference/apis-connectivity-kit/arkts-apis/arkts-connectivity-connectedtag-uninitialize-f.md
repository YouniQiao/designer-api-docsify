# uninitialize

## 导入模块

```TypeScript
import { connectedTag } from 'kits/@kit.ConnectivityKit';
```

## uninitialize

```TypeScript
function uninitialize(): void
```

Uninitializes the connected NFC tag.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**需要权限：** ohos.permission.NFC_TAG

<!--Device-connectedTag-function uninitialize(): void--><!--Device-connectedTag-function uninitialize(): void-End-->

**系统能力：** SystemCapability.Communication.ConnectedTag

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 3200101 | Connected NFC tag running state is abnormal in service. |
| 201 | Permission denied. |

## 示例

```TypeScript
import { connectedTag } from '@kit.ConnectivityKit';

try {
    console.info("connectedTag uninitialize");
    connectedTag.uninitialize();
} catch (error) {
    console.error("connectedTag error: " + error);
}
```

