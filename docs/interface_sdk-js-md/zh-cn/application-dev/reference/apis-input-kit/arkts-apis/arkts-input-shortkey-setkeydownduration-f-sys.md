# setKeyDownDuration（系统接口）

## 导入模块

```TypeScript
import { shortKey } from 'kits/@kit.InputKit';
import { FingerprintEvent } from 'kits/@kit.InputKit';
```

## setKeyDownDuration

```TypeScript
function setKeyDownDuration(businessKey: string, delay: number, callback: AsyncCallback<void>): void
```

设置快捷键拉起Ability的延迟时间，使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.MultimodalInput.Input.ShortKey

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| businessKey | string | 是 |
| delay | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## setKeyDownDuration

```TypeScript
function setKeyDownDuration(businessKey: string, delay: number): Promise<void>
```

设置快捷键拉起Ability的延迟时间，使用Promise异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.MultimodalInput.Input.ShortKey

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| businessKey | string | 是 |
| delay | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
