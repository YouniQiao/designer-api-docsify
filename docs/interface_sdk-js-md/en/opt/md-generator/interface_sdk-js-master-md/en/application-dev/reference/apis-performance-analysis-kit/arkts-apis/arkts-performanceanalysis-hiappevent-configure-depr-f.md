# configure

## Modules to Import

```TypeScript
```

## configure

```TypeScript
function configure(config: ConfigOption): boolean
```

Configures the application event logging function, such as setting the event logging switch and maximum size of the directory that stores the event logging files.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [configure](arkts-performanceanalysis-hiappevent-configure-f.md#configure)

<!--Device-hiAppEvent-function configure(config: ConfigOption): boolean--><!--Device-hiAppEvent-function configure(config: ConfigOption): boolean-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [ConfigOption](arkts-performanceanalysis-hiappevent-configoption-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
// Set the application event logging switch.
let config1: hiAppEvent.ConfigOption = {
  disable: true,
};
hiAppEvent.configure(config1);

// Configure the maximum size of the directory that stores the event logging files.
let config2: hiAppEvent.ConfigOption = {
  maxStorage: '100M',
};
hiAppEvent.configure(config2);
```
