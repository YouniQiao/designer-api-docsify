# isSupported

## 导入模块

```TypeScript
import { cardEmulation } from 'kits/@kit.ConnectivityKit';
```

## isSupported

```TypeScript
function isSupported(feature: number): boolean
```

是否支持某种类型的卡模拟。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [hasHceCapability](arkts-connectivity-cardemulation-hashcecapability-f.md)

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [feature](../../apis-multimodal-awareness-kit/arkts-apis/arkts-multimodalawareness-userstatus-userstatusdata-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
