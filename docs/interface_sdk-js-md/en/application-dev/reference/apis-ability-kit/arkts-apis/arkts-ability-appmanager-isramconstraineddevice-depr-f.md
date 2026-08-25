# isRamConstrainedDevice

## Modules to Import

```TypeScript
```

## isRamConstrainedDevice

```TypeScript
function isRamConstrainedDevice(): Promise<boolean>
```

Checks whether the current device is a RAM-constrained device (a device with severely limited memory resources). This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [isRamConstrainedDevice](arkts-ability-appmanager-isramconstraineddevice-f.md)

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |


## isRamConstrainedDevice

```TypeScript
function isRamConstrainedDevice(callback: AsyncCallback<boolean>): void
```

Checks whether the current device is a RAM-constrained device (a device with severely limited memory resources). This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [isRamConstrainedDevice](arkts-ability-appmanager-isramconstraineddevice-f.md)

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |
