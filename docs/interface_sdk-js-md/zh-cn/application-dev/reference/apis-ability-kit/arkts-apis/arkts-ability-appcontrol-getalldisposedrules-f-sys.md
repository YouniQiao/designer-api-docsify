# getAllDisposedRules（系统接口）

## 导入模块

```TypeScript
import { appControl } from 'kits/@kit.AbilityKit';
```

## getAllDisposedRules

```TypeScript
function getAllDisposedRules(): Array<DisposedRuleConfiguration>
```

获取当前用户下已设置的所有拦截规则。

**起始版本：** 23

**需要权限：** ohos.permission.MANAGE_DISPOSED_APP_STATUS or ohos.permission.GET_DISPOSED_APP_STATUS

**系统能力：** SystemCapability.BundleManager.BundleFramework.AppControl

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Array&lt;[DisposedRuleConfiguration](arkts-ability-appcontrol-disposedruleconfiguration-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
