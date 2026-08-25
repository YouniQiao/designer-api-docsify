# getForegroundApplications (System API)

## Modules to Import

```TypeScript
```

## getForegroundApplications

```TypeScript
function getForegroundApplications(callback: AsyncCallback<Array<AppStateData>>): void
```

getForegroundApplications.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getForegroundApplications](arkts-ability-appmanager-getforegroundapplications-f-sys.md)

**Required permissions:** ohos.permission.GET_RUNNING_INFO

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AppStateData](arkts-ability-appstatedata-c.md)&gt;&gt; | Yes |


## getForegroundApplications

```TypeScript
function getForegroundApplications(): Promise<Array<AppStateData>>
```

getForegroundApplications.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getForegroundApplications](arkts-ability-appmanager-getforegroundapplications-f-sys.md)

**Required permissions:** ohos.permission.GET_RUNNING_INFO

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[AppStateData](arkts-ability-appstatedata-c.md)&gt;&gt; |
