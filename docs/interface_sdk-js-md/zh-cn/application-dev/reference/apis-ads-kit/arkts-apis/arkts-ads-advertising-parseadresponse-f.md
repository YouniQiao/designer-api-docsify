# parseAdResponse

## 导入模块

```TypeScript
import { advertising } from 'kits/@kit.AdsKit';
```

## parseAdResponse

```TypeScript
function parseAdResponse(adResponse: string, listener: MultiSlotsAdLoadListener, context: common.UIAbilityContext): void
```

解析并处理广告响应体（该接口仅对部分系统预置应用开放）。

**起始版本：** 12

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| adResponse | string | 是 |
| listener | [MultiSlotsAdLoadListener](arkts-ads-advertising-multislotsadloadlistener-i.md) | 是 |
| context | common.UIAbilityContext | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [21800001](../errorcode-ads.md#21800001-系统内部错误) |
| [21800005](../errorcode-ads.md#21800005-广告数据解析失败) |
