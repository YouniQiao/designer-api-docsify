# offUpdateFormsConfigCallback（系统接口）

## 导入模块

```TypeScript
import { formHost } from 'kits/@kit.FormKit';
```

## offUpdateFormsConfigCallback

```TypeScript
function offUpdateFormsConfigCallback(callback?: formInfo.UpdateFormsConfigCallback): void
```

取消订阅更新卡片配置事件。使用callback异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | formInfo.UpdateFormsConfigCallback | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
