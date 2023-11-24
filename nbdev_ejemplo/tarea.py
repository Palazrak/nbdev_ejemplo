# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_tarea.ipynb.

# %% auto 0
__all__ = ['Tarea']

# %% ../nbs/00_tarea.ipynb 3
class Tarea:
    "Crea una tarea con un título, una descripción, un estado (completado o no completado) y una fecha de entrega"
    def __init__(self, 
                 titulo:str, # Título de la tarea
                 fecha_entrega:str, # Fecha de entrega en formato dd/mm/aaaa. De no estar escrito así, marcará error
                 completado:bool=False, # Indica si ya se entregó o no
                 descripcion:str='' # Información adicional sobre la tarea
                 ) -> None:
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_entrega = fecha_entrega
        self.completado = completado
    def __str__(self) -> str:
        "Regresa la informacion completa sobre la tarea"
        return f"Tarea: {self.titulo}. \nDescripción: {self.descripcion}. \nFecha de entrega: {self.fecha_entrega}. \nCompletado: {self.completado}"
    __repr__ = __str__ 
    def __lt__(self,
               other: 'Tarea'):
        "Define la lógica de comparación basada en la fecha de entrega"
        return self.fecha_entrega < other.fecha_entrega
