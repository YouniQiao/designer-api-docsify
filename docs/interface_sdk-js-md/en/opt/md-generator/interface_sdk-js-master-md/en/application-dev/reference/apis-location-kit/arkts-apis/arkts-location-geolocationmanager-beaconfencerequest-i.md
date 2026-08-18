# BeaconFenceRequest

Configuring parameters in BeaconFence request.

**Since:** 26.1.0

<!--Device-geoLocationManager-export interface BeaconFenceRequest--><!--Device-geoLocationManager-export interface BeaconFenceRequest-End-->

**System capability:** SystemCapability.Location.Location.Geofence

## Modules to Import

```TypeScript
```

## beacon

```TypeScript
beacon: BeaconFence
```

Beacon fence information.

**Type:** [BeaconFence](arkts-location-geolocationmanager-beaconfence-i.md)

**Since:** 26.1.0

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-BeaconFenceRequest-beacon: BeaconFence--><!--Device-BeaconFenceRequest-beacon: BeaconFence-End-->

**System capability:** SystemCapability.Location.Location.Geofence

## fenceExtensionAbilityName

```TypeScript
fenceExtensionAbilityName?: string
```

Indicates the name of FenceExtensionAbility.

**Type:** string

**Since:** 26.1.0

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-BeaconFenceRequest-fenceExtensionAbilityName?: string--><!--Device-BeaconFenceRequest-fenceExtensionAbilityName?: string-End-->

**System capability:** SystemCapability.Location.Location.Geofence

## transitionCallback

```TypeScript
transitionCallback?: Callback<GeofenceTransition>
```

Indicates the callback for reporting the BeaconFence transition status.

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[GeofenceTransition](arkts-location-geolocationmanager-geofencetransition-i.md)&gt;

**Since:** 26.1.0

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-BeaconFenceRequest-transitionCallback?: Callback<GeofenceTransition>--><!--Device-BeaconFenceRequest-transitionCallback?: Callback<GeofenceTransition>-End-->

**System capability:** SystemCapability.Location.Location.Geofence
