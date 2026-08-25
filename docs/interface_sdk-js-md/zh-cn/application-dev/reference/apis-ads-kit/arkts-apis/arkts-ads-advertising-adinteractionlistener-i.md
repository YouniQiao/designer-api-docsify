# AdInteractionListener

广告状态变化回调。

**起始版本：** 11

**系统能力：** SystemCapability.Advertising.Ads

## 导入模块

```TypeScript
import { advertising } from 'kits/@kit.AdsKit';
```

## onStatusChanged

```TypeScript
onStatusChanged(status: string, ad: Advertisement, data: string)
```

广告状态回调。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| status | string | 是 |
| ad | [Advertisement](arkts-ads-advertisement-advertisement-i.md) | 是 |
| data | string | 是 |
