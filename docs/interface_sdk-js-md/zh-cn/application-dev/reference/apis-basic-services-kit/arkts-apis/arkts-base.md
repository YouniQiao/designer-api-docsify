# @ohos.base(公共回调信息)

本模块定义了OpenHarmony ArkTS接口的公共回调类型，包括接口调用时出现的公共回调和公共错误信息。
 这些回调类型为开发者提供了统一的异步处理机制，适用于需要处理异步操作结果、错误信息回传等场景，可以帮助开发者简化异步编程模型，提高代码的可读性和可维护性。
 > **说明：**
 >
 > - 本模块首批接口从API version 6 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
 > - 从API version 12开始，本模块接口支持在ArkTS卡片中使用。


## 导入模块

```TypeScript
import { AsyncCallback, BusinessError, Callback, ErrorCallback } from '@kit.BasicServicesKit';
import { AsyncCallback, BusinessError, Callback, ErrorCallback, RecordData } from '@kit.BasicServicesKit';
```

## 汇总

### 类

| 名称 |
| --- |
| [BusinessError(公共回调信息)](arkts-basicservices-base-businesserror-c.md) |

### 接口

| 名称 |
| --- |
| [AsyncCallback(公共回调信息)](arkts-basicservices-base-asynccallback-i.md) |
| [BusinessError(公共回调信息)](arkts-basicservices-base-businesserror-i.md) |
| [Callback(公共回调信息)](arkts-basicservices-base-callback-i.md) |
| [ErrorCallback(公共回调信息)](arkts-basicservices-base-errorcallback-i.md) |

### 类型

| 名称 |
| --- |
| [AsyncCallback(公共回调信息)](arkts-basicservices-asynccallback-t.md) |
| [Callback(公共回调信息)](arkts-basicservices-callback-t.md) |
| [ErrorCallback(公共回调信息)](arkts-basicservices-errorcallback-t.md) |
| [RecordData(公共回调信息)](arkts-basicservices-recorddata-t.md) |
