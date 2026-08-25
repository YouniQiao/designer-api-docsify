# getAdRequestBody

## 导入模块

```TypeScript
import { advertising } from 'kits/@kit.AdsKit';
```

## getAdRequestBody

```TypeScript
function getAdRequestBody(adParams: AdRequestParams[], adOptions: AdOptions): Promise<string>
```

获取广告请求体，使用Promise异步回调（该接口仅对部分系统预置应用开放）。

**起始版本：** 12

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| adParams | [AdRequestParams](arkts-ads-advertising-adrequestparams-i.md)[] | 是 |
| [adOptions](arkts-ads-advertising-autoadcomponent-autoadcomponent-s.md) | [AdOptions](arkts-ads-advertising-adoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [21800001](../errorcode-ads.md#21800001-系统内部错误) |
