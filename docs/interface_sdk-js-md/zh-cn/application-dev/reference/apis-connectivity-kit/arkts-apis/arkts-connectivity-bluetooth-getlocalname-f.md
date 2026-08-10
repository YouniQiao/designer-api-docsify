# getLocalName

## 导入模块

```TypeScript
import { bluetooth } from 'kits/@kit.ConnectivityKit';
```

## getLocalName

```TypeScript
function getLocalName(): string
```

Obtains the Bluetooth local name of a device.

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为8。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.getLocalName

**需要权限：** ohos.permission.USE_BLUETOOTH

<!--Device-bluetooth-function getLocalName(): string--><!--Device-bluetooth-function getLocalName(): string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | Returns the name the device. |

## 示例

```TypeScript
let localName : string = bluetooth.getLocalName();
```

