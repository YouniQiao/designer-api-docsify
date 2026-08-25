# switchInputMethod（系统接口）

## 导入模块

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## switchInputMethod

```TypeScript
function switchInputMethod(bundleName: string, subtypeId?: string): Promise<void>
```

切换输入法，使用promise异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.CONNECT_IME_ABILITY

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| subtypeId | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800005](../errorcode-inputmethod-framework.md#12800005-配置持久化失败) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
