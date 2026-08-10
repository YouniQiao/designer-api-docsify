# getCarKeyDfxData（系统接口）

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.ConnectivityKit';
```

## getCarKeyDfxData

```TypeScript
function getCarKeyDfxData(): string
```

Get the dfx data of car key.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-connection-function getCarKeyDfxData(): string--><!--Device-connection-function getCarKeyDfxData(): string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | Returns the dfx data in character string format. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API when the short-range chip is not inserted on the 2in1 device. |
| 202 | Non-system applications are not allowed to use system APIs. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

## 示例

```TypeScript
try {
    let dfxData = connection.getCarKeyDfxData();
} catch (err) {
    console.error(`Failed to get car key dfx data. Code: ${err.code}, message: ${err.message}`);
}
```

