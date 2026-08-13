# setAbilityEnabled（系统接口）

## setAbilityEnabled

```TypeScript
function setAbilityEnabled(info: AbilityInfo, isEnable: boolean, callback: AsyncCallback<void>): void
```

设置是否启用指定的Ability组件，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** null

**需要权限：** ohos.permission.CHANGE_ABILITY_ENABLED_STATE

<!--Device-bundle-function setAbilityEnabled(info: AbilityInfo, isEnable: boolean, callback: AsyncCallback<void>): void--><!--Device-bundle-function setAbilityEnabled(info: AbilityInfo, isEnable: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [AbilityInfo](arkts-ability-abilityinfo-abilityinfo-depr-i.md) | 是 |
| isEnable | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## setAbilityEnabled

```TypeScript
function setAbilityEnabled(info: AbilityInfo, isEnable: boolean): Promise<void>
```

设置是否启用指定的Ability组件，使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** null

**需要权限：** ohos.permission.CHANGE_ABILITY_ENABLED_STATE

<!--Device-bundle-function setAbilityEnabled(info: AbilityInfo, isEnable: boolean): Promise<void>--><!--Device-bundle-function setAbilityEnabled(info: AbilityInfo, isEnable: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [AbilityInfo](arkts-ability-abilityinfo-abilityinfo-depr-i.md) | 是 |
| isEnable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
