# killProcessesByBundleName（系统接口）

## 导入模块

```TypeScript
```

## killProcessesByBundleName

```TypeScript
function killProcessesByBundleName(bundleName: string): Promise<void>
```

通过Bundle名称终止进程。使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [killProcessesByBundleName](arkts-ability-appmanager-killprocessesbybundlename-f.md)

**需要权限：** ohos.permission.CLEAN_BACKGROUND_PROCESSES

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |


## killProcessesByBundleName

```TypeScript
function killProcessesByBundleName(bundleName: string, callback: AsyncCallback<void>)
```

通过Bundle名称终止进程。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [killProcessesByBundleName](arkts-ability-appmanager-killprocessesbybundlename-f.md)

**需要权限：** ohos.permission.CLEAN_BACKGROUND_PROCESSES

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |
