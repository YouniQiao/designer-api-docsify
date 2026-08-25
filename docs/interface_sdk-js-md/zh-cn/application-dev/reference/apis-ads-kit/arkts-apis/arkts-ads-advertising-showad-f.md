# showAd

## 导入模块

```TypeScript
import { advertising } from 'kits/@kit.AdsKit';
```

## showAd

```TypeScript
function showAd(ad: Advertisement, options: AdDisplayOptions, context?: common.UIAbilityContext): void
```

展示全屏广告。

> **说明：**&gt;
> 1. 为了保证广告能正确展示，该接口必须和请求广告接口配套使用。&gt;
> 2. 该接口仅支持展示激励广告和插屏广告。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ad | [Advertisement](arkts-ads-advertisement-advertisement-i.md) | 是 |
| options | [AdDisplayOptions](arkts-ads-advertising-addisplayoptions-i.md) | 是 |
| context | common.UIAbilityContext | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [21800001](../errorcode-ads.md#21800001-系统内部错误) |
| [21800004](../errorcode-ads.md#21800004-广告展示失败) |
