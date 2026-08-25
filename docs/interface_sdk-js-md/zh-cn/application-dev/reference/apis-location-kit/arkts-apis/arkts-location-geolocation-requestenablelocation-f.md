# requestEnableLocation

## 导入模块

```TypeScript
import { geolocation } from 'kits/@kit.LocationKit';
```

## requestEnableLocation

```TypeScript
function requestEnableLocation(callback: AsyncCallback<boolean>): void
```

请求打开位置服务，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**需要权限：** ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |


## requestEnableLocation

```TypeScript
function requestEnableLocation(): Promise<boolean>
```

请求打开位置服务，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**需要权限：** ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |
