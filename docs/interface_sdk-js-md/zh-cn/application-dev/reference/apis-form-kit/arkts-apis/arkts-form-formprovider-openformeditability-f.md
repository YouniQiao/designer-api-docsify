# openFormEditAbility

## 导入模块

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## openFormEditAbility

```TypeScript
function openFormEditAbility(abilityName: string, formId: string, isMainPage?: boolean): void
```

打开卡片编辑页。适用于需要用户配置卡片参数的场景，例如设置卡片显示内容、选择数据源、配置更新频率等。

**起始版本：** 18

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| abilityName | string | 是 |
| formId | string | 是 |
| isMainPage | boolean | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [16500100](../errorcode-form.md#16500100-获取卡片配置信息失败) |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |
| [16501003](../errorcode-form.md#16501003-无法操作指定卡片) |
| [16501007](../errorcode-form.md#16501007-卡片不可信) |
