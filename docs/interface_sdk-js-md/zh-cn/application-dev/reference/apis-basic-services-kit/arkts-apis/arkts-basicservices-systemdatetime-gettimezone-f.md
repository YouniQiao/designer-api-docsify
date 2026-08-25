# getTimezone

## 导入模块

```TypeScript
import { systemDateTime } from 'kits/@kit.BasicServicesKit';
```

## getTimezone

```TypeScript
function getTimezone(callback: AsyncCallback<string>): void
```

获取系统时区，使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |


## getTimezone

```TypeScript
function getTimezone(): Promise<string>
```

获取系统时区，使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.MiscServices.Time

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |
