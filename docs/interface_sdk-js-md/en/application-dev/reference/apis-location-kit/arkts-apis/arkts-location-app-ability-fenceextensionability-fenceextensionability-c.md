# FenceExtensionAbility

Class of fence extension ability.

**Since:** 14

**System capability:** SystemCapability.Location.Location.Geofence

## Modules to Import

```TypeScript
import { FenceExtensionAbility } from 'kits/@kit.LocationKit';
```

## onDestroy

```TypeScript
onDestroy(): void
```

Called back before a fence extension is destroyed.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Location.Location.Geofence

## onFenceStatusChange

```TypeScript
onFenceStatusChange(transition: geoLocationManager.GeofenceTransition, additions: Record<string, string>): void
```

Called back when geofence status is change.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Location.Location.Geofence

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| transition | geoLocationManager.GeofenceTransition | Yes |
| additions | Record & lt;string, string & gt; | Yes |

## context

```TypeScript
context: FenceExtensionContext
```

Indicates the fence extension context.

**Type:** [FenceExtensionContext](arkts-location-app-ability-fenceextensioncontext-fenceextensioncontext-c-sys.md)

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Location.Location.Geofence
