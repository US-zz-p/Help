"""
.. module:: useful_1
   :platform: Unix, Windows
   :synopsis: A useful module indeed.

.. moduleauthor:: Andrew Carter <andrew@invalid.com>


"""


def public_fn_with_googley_docstring(name, state=None):
    r"""This function does something.

    Args:
       name (str):  The name to use.

    Kwargs:
       state (bool): Current state to be in.

    Returns:
       int.  The return code::

          0 -- Success!
          1 -- No good.
          2 -- Try again.

    Raises:
       AttributeError, KeyError

    A really great idea.  A way you might use me is

    >>> print public_fn_with_googley_docstring(name='foo', state=None)
    0

    BTW, this always returns 0.  **NEVER** use with :class:`MyPublicClass`.

    .. math::
        :nowrap:

        \begin{eqnarray}
          y    & = & ax^2 + bx + c \\
          f(x) & = & x^2 + 2xy + y^2
        \end{eqnarray}
    """
    return 0


def public_fn_with_sphinxy_docstring(name, state=None):
    r"""This function does something.

    :param name: The name to use.
    :type name: str.
    :param state: Current state to be in.
    :type state: bool.
    :returns:  int -- the return code.
    :raises: AttributeError, KeyError


    .. math::
        W^{3\beta}_{\delta_1 \rho_1 \sigma_2} \approx U^{3\beta}_{\delta_1 \rho_1}


    .. math::
        \langle \alpha, \beta  \rangle
        \in
        \Biggl \lbrace
        {
        M,\text{ if }
           {
            l(\underline{x}) =
              \frac { p(\underline{x}|M ) } { p(\underline{x}|U) }
              \geq
               \frac { p(U) }{ p(M) } }
        \atop
        U, \text{ otherwise }
        }
    """
    return 0


def public_fn_without_docstring():
    return True


def _private_fn_with_docstring(foo, bar='baz', foobarbas=None):
    """I have a docstring, but won't be imported if you just use ``:members:``.
    """
    return None


class MyPublicClass(object):
    r"""We use this as a public class example class.

    You never call this class before calling :func:`public_fn_with_sphinxy_docstring`.

    .. math::
        W^{3\beta}_{\delta_1 \rho_1 \sigma_2} \approx U^{3\beta}_{\delta_1 \rho_1}

    .. note::
       An example of intersphinx is this: you **cannot** use :mod:`pickle` on this class.

    """

    def __init__(self, foo, bar='baz'):
        r"""A really simple class.

        Args:
           foo (str): We all know what foo does.

        Kwargs:
           bar (str): Really, same as foo.

        """
        self._foo = foo
        self._bar = bar

    def get_foobar(self, foo, bar=True):
        r"""This gets the foobar

        This really should have a full function definition, but I am too lazy.

        >>> print get_foobar(10, 20)
        30
        >>> print get_foobar('a', 'b')
        ab

        Isn't that what you want?

        Since Pythagoras, we know that: :math:`a^2 + b^2 = c^2`.

        Formula 1: :math:`(a + b)^2 = a^2 + 2ab + b^2`

        Formula 2:

        .. math::
            \sum^{+\infty}_{i = 1} \alpha^i \cdots \frac{\partial f}{\partial x}

        Formula 3:

        .. math::
            (a + b)^2  &=  (a + b)(a + b) \\
                        &=  a^2 + 2ab + b^2

        Formula 4: :math:`\sum^{+\infty}_{i = 1} \alpha^i \cdots \frac{\partial f}{\partial x}`

        Formula 5:

        .. math::
            e^{i\pi} + 1 = 0
            :label: euler
        """

        "Comment above the line"
        self.test = 'test'  # commenting this line

        """ commenting return """
        self.test2 = 'test2'

        ''' another comment '''
        return foo + bar

    def _get_baz(self, baz=None):
        """A private function to get baz.

        This really should have a full function definition, but I am too lazy.

        """
        return baz

    def test1(self):
        """
        Euler's identity, equation :eq:`euler`, was elected one of the most beautiful mathematical formulas.
        """


print('Useful 1')
