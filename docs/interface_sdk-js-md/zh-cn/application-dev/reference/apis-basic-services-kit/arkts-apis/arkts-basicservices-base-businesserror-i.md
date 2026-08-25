# BusinessError

错误参数，继承自Error类，用于在接口调用失败时传递标准化的错误信息，包含错误码和可选的附加信息。

**继承/实现关系：** BusinessError extends Error

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为6。

**系统能力：** SystemCapability.Base

## 导入模块

```TypeScript
import { AsyncCallback, BusinessError, Callback, ErrorCallback } from '@kit.BasicServicesKit';
import { AsyncCallback, BusinessError, Callback, ErrorCallback, RecordData } from '@kit.BasicServicesKit';
```

## constructor

```TypeScript
constructor()
```

BusinessError的构造函数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Base

## constructor

```TypeScript
constructor(code: int, error: Error)
```

BusinessError的构造函数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Base

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [code](#code) | int | 是 |
| error | Error | 是 |

## constructor

```TypeScript
constructor(code: int, data: T, error: Error)
```

BusinessError的构造函数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Base

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [code](#code) | int | 是 |
| [data](#data) | T | 是 |
| error | Error | 是 |

## constructor

```TypeScript
constructor(code: int, message: string, data?: T)
```

BusinessError的构造函数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Base

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [code](#code) | int | 是 |
| message | string | 是 |
| [data](#data) | T | 否 |

## code

```TypeScript
code: number
```

接口调用失败返回的错误码信息。具体错误码值由各接口定义，请参考对应接口的错误码说明。

**类型：** number

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为6。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Base

## data

```TypeScript
data?: T
```

接口调用失败时返回的附加错误信息。如果不填，则错误对象不包含附加数据。

**类型：** T

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Base
