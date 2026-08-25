# isRequestPublishFormSupported（系统接口）

## 导入模块

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## isRequestPublishFormSupported

```TypeScript
function isRequestPublishFormSupported(callback: AsyncCallback<boolean>): void
```

查询是否可以发布卡片到卡片使用方，使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |


## isRequestPublishFormSupported

```TypeScript
function isRequestPublishFormSupported(): Promise<boolean>
```

查询是否可以发布卡片到卡片使用方，使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |
