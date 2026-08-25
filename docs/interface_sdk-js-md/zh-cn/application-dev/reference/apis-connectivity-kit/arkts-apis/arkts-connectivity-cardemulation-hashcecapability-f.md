# hasHceCapability

## 导入模块

```TypeScript
import { cardEmulation } from 'kits/@kit.ConnectivityKit';
```

## hasHceCapability

```TypeScript
function hasHceCapability(): boolean
```

判断设备是否支持HCE卡模拟功能。

**起始版本：** 9

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
