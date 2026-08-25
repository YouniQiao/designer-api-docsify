# AdLoader

提供加载广告的功能。

**起始版本：** 11

**系统能力：** SystemCapability.Advertising.Ads

## 导入模块

```TypeScript
import { advertising } from 'kits/@kit.AdsKit';
```

## constructor

```TypeScript
constructor(context: common.Context)
```

构造函数。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | common.Context | 是 |

## loadAd

```TypeScript
loadAd(adParam: AdRequestParams, adOptions: AdOptions, listener: AdLoadListener): void
```

请求单广告位广告。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [adParam](arkts-ads-advertising-autoadcomponent-autoadcomponent-s.md) | [AdRequestParams](arkts-ads-advertising-adrequestparams-i.md) | 是 |
| [adOptions](arkts-ads-advertising-autoadcomponent-autoadcomponent-s.md) | [AdOptions](arkts-ads-advertising-adoptions-i.md) | 是 |
| listener | [AdLoadListener](arkts-ads-advertising-adloadlistener-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [21800001](../errorcode-ads.md#21800001-系统内部错误) |
| [21800003](../errorcode-ads.md#21800003-广告请求加载失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## loadAdWithMultiSlots

```TypeScript
loadAdWithMultiSlots(adParams: AdRequestParams[], adOptions: AdOptions, listener: MultiSlotsAdLoadListener): void
```

请求多广告位广告。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| adParams | [AdRequestParams](arkts-ads-advertising-adrequestparams-i.md)[] | 是 |
| [adOptions](arkts-ads-advertising-autoadcomponent-autoadcomponent-s.md) | [AdOptions](arkts-ads-advertising-adoptions-i.md) | 是 |
| listener | [MultiSlotsAdLoadListener](arkts-ads-advertising-multislotsadloadlistener-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [21800001](../errorcode-ads.md#21800001-系统内部错误) |
| [21800003](../errorcode-ads.md#21800003-广告请求加载失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
