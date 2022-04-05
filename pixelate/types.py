import click
import typing as t


class ResizeType(click.ParamType):
    """An image resize spec type"""
    name = "resize"

    def convert(
        self,
        value: t.Any,
        param: t.Optional["click.Parameter"],
        ctx: t.Optional["click.Context"],
    ) -> t.Any:
        if isinstance(value, (float, tuple)):
            return value
        
        lowered = value.lower()
        
        try:
            # parse 20x20 as a tuple
            if "x" in lowered:
                dims = lowered.split("x")
                if len(dims) != 2:
                    raise ValueError
                return (int(dims[0]), int(dims[1]))

            # parse 50% as 0.5
            if "%" in lowered:
                return float(lowered[:-1]) / 100
            
            return float(lowered)
        except ValueError:
            self.fail(f"{value} is not a valid resize option. For example, use 20x20, 50%, or 0.5.")
