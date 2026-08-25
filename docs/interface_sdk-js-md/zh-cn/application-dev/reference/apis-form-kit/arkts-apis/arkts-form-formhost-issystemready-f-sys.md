# isSystemReady（系统接口）

## 导入模块

```TypeScript
import { formHost } from 'kits/@kit.FormKit';
```

## isSystemReady

```TypeScript
function isSystemReady(callback: AsyncCallback<void>): void
```

检查系统是否准备好。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## isSystemReady

```TypeScript
function isSystemReady(): Promise<void>
```

检查系统是否准备好。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
