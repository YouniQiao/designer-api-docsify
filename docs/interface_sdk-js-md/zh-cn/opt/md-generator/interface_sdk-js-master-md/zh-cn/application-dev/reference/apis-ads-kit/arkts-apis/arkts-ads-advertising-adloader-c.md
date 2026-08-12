# AdLoader

提供加载广告的功能。

**起始版本：** 11

<!--Device-advertising-export class AdLoader--><!--Device-advertising-export class AdLoader-End-->

**系统能力：** SystemCapability.Advertising.Ads

## constructor

```TypeScript
constructor(context: common.Context)
```

构造函数。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AdLoader-constructor(context: common.Context)--><!--Device-AdLoader-constructor(context: common.Context)-End-->

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | common.Context | 是 |

## 示例

其中context的获取方式参见[各类context的获取方式](../../application-models/application-context-stage.md#context的获取方式)。

```TypeScript
import { common } from '@kit.AbilityKit';
import { advertising } from '@kit.AdsKit';
// ...

function createAdLoader(context: common.Context): void {
  const adLoader: advertising.AdLoader = new advertising.AdLoader(context);
}
```

## loadAd

```TypeScript
loadAd(adParam: AdRequestParams, adOptions: AdOptions, listener: AdLoadListener): void
```

请求单广告位广告。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AdLoader-loadAd(adParam: AdRequestParams, adOptions: AdOptions, listener: AdLoadListener): void--><!--Device-AdLoader-loadAd(adParam: AdRequestParams, adOptions: AdOptions, listener: AdLoadListener): void-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [21800001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ads-kit/errorcode-ads.md#21800001-系统内部错误) |
| [21800003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ads-kit/errorcode-ads.md#21800003-广告请求加载失败) |

## 示例

其中context的获取方式参见[各类context的获取方式](../../application-models/application-context-stage.md#context的获取方式)。

```TypeScript
import { common } from '@kit.AbilityKit';
import { advertising } from '@kit.AdsKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// ...
function loadAd(context: common.Context, adRequestParams: advertising.AdRequestParams): void {
  // 广告配置参数，开发者可根据项目实际情况设置
  const adOptions: advertising.AdOptions = {};
  // 广告请求回调监听
  const adLoaderListener: advertising.AdLoadListener = {
    onAdLoadFailure: (errorCode: number, errorMsg: string) => {
      hilog.error(0x0000, 'testTag', `Failed to load ad. Code is ${errorCode}, message is ${errorMsg}`);
    },
    onAdLoadSuccess: (ads: Array<advertising.Advertisement>) => {
      hilog.info(0x0000, 'testTag', 'Succeeded in loading ad');
      // 保存请求到的广告内容用于展示
      const returnAds: advertising.Advertisement[] = ads;
    }
  };
  // 创建AdLoader广告对象
  const adLoader: advertising.AdLoader = new advertising.AdLoader(context);
  // 调用广告请求接口
  adLoader.loadAd(adRequestParams, adOptions, adLoaderListener);
}
```

## loadAdWithMultiSlots

```TypeScript
loadAdWithMultiSlots(adParams: AdRequestParams[], adOptions: AdOptions, listener: MultiSlotsAdLoadListener): void
```

请求多广告位广告。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AdLoader-loadAdWithMultiSlots(adParams: AdRequestParams[], adOptions: AdOptions, listener: MultiSlotsAdLoadListener): void--><!--Device-AdLoader-loadAdWithMultiSlots(adParams: AdRequestParams[], adOptions: AdOptions, listener: MultiSlotsAdLoadListener): void-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [21800001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ads-kit/errorcode-ads.md#21800001-系统内部错误) |
| [21800003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ads-kit/errorcode-ads.md#21800003-广告请求加载失败) |

## 示例

其中context的获取方式参见[各类context的获取方式](../../application-models/application-context-stage.md#context的获取方式)。

```TypeScript
import { common } from '@kit.AbilityKit';
import { advertising } from '@kit.AdsKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// ...
function loadAdWithMultiSlots(context: common.Context, adRequestParamsArray: advertising.AdRequestParams[]): void {
  // 广告配置参数，开发者可根据项目实际情况设置
  const adOptions: advertising.AdOptions = {};
  // 广告请求回调监听
  const multiSlotsAdLoaderListener: advertising.MultiSlotsAdLoadListener = {
    onAdLoadFailure: (errorCode: number, errorMsg: string) => {
      hilog.error(0x0000, 'testTag', `Failed to load multiSlots ad. Code is ${errorCode}, message is ${errorMsg}`);
    },
    onAdLoadSuccess: (ads: Map<string, Array<advertising.Advertisement>>) => {
      hilog.info(0x0000, 'testTag', 'Succeeded in loading multiSlots ad');
      // 保存请求到的广告内容用于展示
      const returnAds: advertising.Advertisement[] = [];
      ads.forEach((adsArray) => returnAds.push(...adsArray));
    }
  };
  // 创建AdLoader广告对象
  const adLoader: advertising.AdLoader = new advertising.AdLoader(context);
  // 调用广告请求接口
  adLoader.loadAdWithMultiSlots(adRequestParamsArray, adOptions, multiSlotsAdLoaderListener);
}
```
