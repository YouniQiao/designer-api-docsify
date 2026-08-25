# DeviceTypes

Enumerates device types, which can be used to verify the return value of **deviceType**.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**System capability:** SystemCapability.Startup.SystemInfo

## TYPE_DEFAULT

```TypeScript
TYPE_DEFAULT = 'default'
```

Default device

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Startup.SystemInfo

## TYPE_PHONE

```TypeScript
TYPE_PHONE = 'phone'
```

Smartphone

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Startup.SystemInfo

## TYPE_TABLET

```TypeScript
TYPE_TABLET = 'tablet'
```

Tablet

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Startup.SystemInfo

## TYPE_2IN1

```TypeScript
TYPE_2IN1 = '2in1'
```

PC/2-in-1 device

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Startup.SystemInfo

## TYPE_TV

```TypeScript
TYPE_TV = 'tv'
```

Smart TV

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Startup.SystemInfo

## TYPE_WEARABLE

```TypeScript
TYPE_WEARABLE = 'wearable'
```

Wearable

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Startup.SystemInfo

## TYPE_CAR

```TypeScript
TYPE_CAR = 'car'
```

Head unit

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Startup.SystemInfo

**Examples**

```TypeScript
let deviceTypesInfoDefault: string = deviceInfo.DeviceTypes.TYPE_DEFAULT;
    // Output: the value of the DeviceTypes is :default
    console.info('the value of the DeviceTypes is :' + deviceTypesInfoDefault);

    let deviceTypesInfoPhone: string = deviceInfo.DeviceTypes.TYPE_PHONE;
    // Output: the value of the DeviceTypes is :phone-type 
    console.info('the value of the DeviceTypes is :' + deviceTypesInfoPhone);

    let deviceTypesInfoTablet: string = deviceInfo.DeviceTypes.TYPE_TABLET;
    // Output: the value of the DeviceTypes is :tablet
    console.info('the value of the DeviceTypes is :' + deviceTypesInfoTablet);

    let deviceTypesInfo2IN1: string = deviceInfo.DeviceTypes.TYPE_2IN1;
    // Output: the value of the DeviceTypes is :2in1
    console.info('the value of the DeviceTypes is :' + deviceTypesInfo2IN1);

    let deviceTypesInfoTV: string = deviceInfo.DeviceTypes.TYPE_TV;
    // Output: the value of the DeviceTypes is :tv
    console.info('the value of the DeviceTypes is :' + deviceTypesInfoTV);

    let deviceTypesInfoWearable: string = deviceInfo.DeviceTypes.TYPE_WEARABLE;
    // Output: the value of the DeviceTypes is :wearable
    console.info('the value of the DeviceTypes is :' + deviceTypesInfoWearable);

    let deviceTypesInfoCar: string = deviceInfo.DeviceTypes.TYPE_CAR;
    // Output: the value of the DeviceTypes is :car
    console.info('the value of the DeviceTypes is :' + deviceTypesInfoCar);
```
