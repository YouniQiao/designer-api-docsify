# setCarKeyDfxData（系统接口）

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.ConnectivityKit';
```

## setCarKeyDfxData

```TypeScript
function setCarKeyDfxData(deviceId: string, action: CarKeyActionType): void
```

Set the dfx data of car key.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-connection-function setCarKeyDfxData(deviceId: string, action: CarKeyActionType): void--><!--Device-connection-function setCarKeyDfxData(deviceId: string, action: CarKeyActionType): void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | Indicates device ID. For example, "11:22:33:AA:BB:FF". |
| action | [CarKeyActionType](arkts-connectivity-connection-carkeyactiontype-e-sys.md) | 是 | Indicates the action to set the data. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API when the short-range chip is not inserted on 2in1 device. |
| 202 | Non-system applications are not allowed to use system APIs. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

## 示例

```TypeScript
try {
    connection.setCarKeyDfxData('11:22:33:44:55:66', connection.CarKeyActionType.CAR_KEY_ACTION_ADD);
} catch (err) {
    console.error(`Failed to set car key dfx data. Code: ${err.code}, message: ${err.message}`);
}
```

