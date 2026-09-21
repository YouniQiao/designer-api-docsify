# WithEnv(Define the WithEnv component that allows setting environment properties for child components.)

The **WithEnv** component is used to set a local environment variable scope for a child component tree. Developers can use this component to provide custom environment variables for descendant components, or set system environment variables.

> **NOTE** > > - Custom environment variables can be set through [customEnv](arkts-arkui-withenv-comp-attribute.md#customenv). > - System environment variable keys can be set through [env](arkts-arkui-withenv-comp-attribute.md#env). They are stored in > [WritableEnvKey](arkts-arkui-common-comp-writableenvkey-c.md). > - When **WithEnv** is nested, the nearest scope takes effect for environment variables with the same name.

## Summary

## Examples

```TypeScript
### Example 1: Setting Local Font Scale

This example uses  to set a local font scale for components within the scope.

Since API version 26.0.0, the env attribute and the key WritableEnvKey.FONT_SCALE are added.
```

```TypeScript
### Example 2: Setting Local Layout Direction

This example uses  to set the local layout direction for components within the scope.

Since API version 26.0.0, the env attribute and the key WritableEnvKey.DIRECTION are added.
```
