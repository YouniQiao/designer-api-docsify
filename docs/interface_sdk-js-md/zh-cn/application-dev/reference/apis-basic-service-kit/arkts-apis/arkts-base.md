# @ohos.base

本模块定义了OpenHarmony ArkTS接口的公共回调类型，包括接口调用时出现的公共回调和公共错误信息。
 > **说明**
 >
 > - 本模块首批接口从API version 6 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
 >
 > - 从API version 12开始，本模块接口支持在ArkTS卡片中使用。


## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [BusinessError](arkts-basicservices-base-businesserror-c.md) | 错误参数。 |

### 类型

| 名称 | 说明 |
| --- | --- |
| [AsyncCallback](arkts-basicservices-asynccallback-t.md) | 通用回调函数，携带错误参数和异步返回值。错误参数为[BusinessError]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_类型的信息。异步返回值的类型由开发者自定义，回调将返回对应类型的信息。 |
| [Callback](arkts-basicservices-callback-t.md) | 通用回调函数。开发者在使用时，可自定义data的类型，回调将返回对应类型的信息。 |
| [ErrorCallback](arkts-basicservices-errorcallback-t.md) | 通用回调函数，携带错误参数。回调返回的信息为[BusinessError]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_类型的信息。 |
| [RecordData](arkts-basicservices-recorddata-t.md) | RecordData 是一个联合类型，用于层级和每层数量都不确定的对象结构。 |

