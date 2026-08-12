# setFoldStatusLocked（系统接口）

## setFoldStatusLocked

```TypeScript
function setFoldStatusLocked(locked: boolean): void
```

设置可折叠设备当前折叠状态的锁定状态。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-display-function setFoldStatusLocked(locked: boolean): void--><!--Device-display-function setFoldStatusLocked(locked: boolean): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locked | boolean | 是 | 可折叠设备的折叠状态是否锁定。true表示锁定，false表示不锁定。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| [1400003](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-arkui/errorcode-display.md#1400003-系统服务工作异常) | This display manager service works abnormally. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Permission verification failed. A non-system application calls a system API. |

## 示例

ArkTS-Dyn示例：

```TypeScript
import { display } from '@kit.ArkUI';

try {
  let locked: boolean = false;
  // 设置折叠状态不锁定
  display.setFoldStatusLocked(locked);
} catch (exception) {
  console.error(`Failed to change the fold status locked mode. Code: ${exception.code}, message: ${exception.message}`);
}
```

ArkTS-Sta示例：

```TypeScript
import { display } from '@kit.ArkUI';

try {
  let locked: boolean = false;
  display.setFoldStatusLocked(locked);
} catch (exception) {
  let error = exception as BusinessError;
  console.error(`Failed to change the fold status locked mode. Code: ${error.code} , message: ${error.message}`);
}
```

