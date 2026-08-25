# offFormUninstall（系统接口）

## 导入模块

```TypeScript
import { formHost } from '@kit.FormKit';
```

## offFormUninstall

```TypeScript
function offFormUninstall(callback?: Callback<string>): void
```

Cancels listening to the event of uninstall form.You can use this method to cancel listening to the event of uninstall form.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
'use static'

import { formHost } from '@kit.FormKit';

try {
  formHost.offFormUninstall();
} catch (error) {
  console.error(`catch error, code: ${error.code}, message: ${error.message}`);
}
```
