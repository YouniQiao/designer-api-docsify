# AdLoadListener

单广告位广告请求回调。

**起始版本：** 11

**系统能力：** SystemCapability.Advertising.Ads

## 导入模块

```TypeScript
import { advertising } from 'kits/@kit.AdsKit';
```

## onAdLoadFailure

```TypeScript
onAdLoadFailure(errorCode: number, errorMsg: string): void
```

广告请求失败回调。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| errorCode | number | 是 |
| [errorMsg](../../apis-avsession-kit/arkts-apis/arkts-avsession-avmusictemplate-operresult-i.md) | string | 是 |

## onAdLoadSuccess

```TypeScript
onAdLoadSuccess(ads: Array<Advertisement>): void
```

广告请求成功后回调。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [ads](arkts-ads-advertising-adcomponent-adcomponent-s.md) | Array & lt;Advertisement & gt; | 是 |
